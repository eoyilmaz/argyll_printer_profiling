# -*- coding: utf-8 -*-
import glob
import os
import pytest
import logging

from icc_generator.api import ICCGenerator

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@pytest.fixture(scope="function")
def file_collector():
    """Collect files."""
    files_and_folders = []
    yield files_and_folders

    logger.debug("===========================")
    logger.debug("Removing collected file paths")
    for f in files_and_folders:
        f = os.path.expandvars(os.path.expanduser(f))
        if os.path.exists(f):
            logger.debug("removing: %s" % f)
            if os.path.isdir(f):
                try:
                    os.removedirs(f)
                except OSError:
                    pass
                    # the directory is not empty
                    # remove all the files under it
                    # and then try again
                    for d in glob.glob("%s/*" % f):
                        # print("%s" % d)
                        os.remove(d)
                    try:
                        os.removedirs(f)
                    except OSError:
                        pass
            elif os.path.isfile(f):
                os.remove(f)
    logger.debug("End of collected file paths")
    logger.debug("===========================")


@pytest.fixture(scope="function")
def patch_run_external_process():
    """patches the given function"""
    orig_method = ICCGenerator.run_external_process
    commands = []

    def patched_run_external_process(self, command, shell=False):
        commands.append(command)
        yield ""

    ICCGenerator.run_external_process = patched_run_external_process
    yield commands
    ICCGenerator.run_external_process = orig_method


@pytest.fixture(scope="function")
def patch_run_external_process_class_method_version():
    """patches the given function."""
    orig_method = ICCGenerator.run_external_process

    commands = []

    def patched_run_external_process(command, shell=False):
        commands.append(command)
        yield ""

    ICCGenerator.run_external_process = patched_run_external_process

    yield commands

    ICCGenerator.run_external_process = orig_method


@pytest.fixture(scope="function")
def set_to_windows():
    """patches os.name to nt."""
    orig_value = os.name
    os.name = "nt"
    yield None
    os.name = orig_value


@pytest.fixture(scope="function")
def set_to_linux():
    """patches os.name to posix."""
    orig_value = os.name
    os.name = "posix"
    yield None
    os.name = orig_value
