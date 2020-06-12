from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class Zookeeper(StageTest):
    def generate(self):
        return [TestCase(attach=
                         "I do love animals!\n"
                         "Start looking after animals...\n"
                         "Deer looks fine.\n"
                         "Bat looks happy.\n"
                         "Lion looks healthy.")]

    def check(self, reply, attach):
        if attach not in reply.strip():
            return CheckResult.wrong('Your output should be like in the example!')
        return CheckResult.correct()


if __name__ == '__main__':
    Zookeeper('zookeeper.zookeeper').run_tests()
