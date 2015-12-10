#!/usr/bin/env python3

"""
Author: Tigran Hakobyan (tik.hakobyan@gmail.com)
"""
import sys
import json


class Question(object):

    def __init__(self, key, text, topics):
        self.key = key
        self.text = text
        self.topics = topics


class Topic(object):

    def __init__(self, name, followers):
        self.name = name
        self.followers = followers


class DuplicatesAnalyzer(object):

    all_questions_map = {}
    all_known_duplicates = {}

    def execute(self, expected_input):
        """
        Get an expected input string and execute duplicate validation.
        Two questions are duplicate if one of below conditions are met.
        1. Both questions have exactly the same question text.
        2. Transitive rule works. Q1' is duplicate qith Q2' (Q2' is the known pair of Q1)
        3. Q1 and Q2 share 2 or more common topics.
        """
        all_lines = expected_input.splitlines()

        current_line = 0
        q = int(all_lines[0])
        for i in range(q):
            current_line = current_line + 1
            json_question = json.loads(all_lines[current_line])
            # create a list of all topics of the question
            all_topics = [Topic(t["name"], t["followers"]) for t in json_question["topics"]]
            # create a question and add it into the hash table for faster lookup
            key = json_question["question_key"]
            # create a question object
            question = Question(key=key, topics=all_topics, text=json_question["question_text"])
            self.all_questions_map[key] = question

        # process all known question pairs and store them in a hash table
        current_line = current_line + 1
        d = int(all_lines[current_line])
        for j in range(d):
            current_line = current_line + 1
            question_keys = all_lines[current_line].split()
            if question_keys[2] == '1':
                self.all_known_duplicates[question_keys[0]] = question_keys[1]
                # also the opposite mapping of the keys to make lookup easier
                # for transitive relation rule
                self.all_known_duplicates[question_keys[1]] = question_keys[0]

        # start processing all unknown questions
        current_line = current_line + 1
        n = int(all_lines[current_line])

        for k in range(n):
            current_line = current_line + 1
            questions_pair = all_lines[current_line].split()
            q1_key = questions_pair[0]
            q2_key = questions_pair[1]
            is_duplicate = False

            # check if both questions have exactly same text
            if self.all_questions_map[q1_key].text == self.all_questions_map[q2_key].text:
                is_duplicate = True
            # check if questions are duplicates by transitive relation.
            # Uses already known pair list.
            elif self.check_transitive_relation(q1_key, q2_key):
                is_duplicate = True
            # check two see if questions share at least 2 topics
            elif len(self.get_common_topics(q1_key, q2_key)) >= 2:
                is_duplicate = True

            print("{0} {1} {2}".format(q1_key, q2_key, int(is_duplicate)))

    def check_transitive_relation(self, q1_key, q2_key):
        if q1_key in self.all_known_duplicates and q2_key in self.all_known_duplicates:
            q1_key_duplicate = self.all_known_duplicates[q1_key]
            q2_key_duplicate = self.all_known_duplicates[q2_key]
            if q1_key_duplicate == q2_key or q2_key_duplicate == q1_key or q1_key_duplicate == q2_key_duplicate:
                return True

        if q1_key in self.all_known_duplicates:
            q1_key_duplicate = self.all_known_duplicates[q1_key]
            if q1_key_duplicate == q2_key:
                return True

        if q2_key in self.all_known_duplicates:
            q2_key_duplicate = self.all_known_duplicates[q2_key]
            if q2_key_duplicate == q1_key:
                return True

        return False

    def get_common_topics(self, q1_key, q2_key):
        # intersection of sets is O(1) so let's convert the list to a set
        q1_topics_name_set = set(topic.name for topic in self.all_questions_map[q1_key].topics)
        q2_topics_name_set = set(topic.name for topic in self.all_questions_map[q2_key].topics)

        return q1_topics_name_set.intersection(q2_topics_name_set)


if __name__ == "__main__":
    DuplicatesAnalyzer().execute(open(sys.argv[1]).read())
