
from buildbot.steps.shell import WarningCountingShellCommand


class CMakeBuild(WarningCountingShellCommand):

    name = 'cmakebuild'
    haltOnFailure = 1
    flunkOnFailure = 1
    description = ['building', 'with', 'cmake']
    descriptionDone = ['cmake', 'build']
    command = ["cmake", "--build", "."]
