import argparse
import collections
import configparser
import hashlib
import os
import sys
import zlib

argparser = argparse.ArgumentParser(description="The stupid content tracker")

argsubparsers = argparser.add_subparsers(title="Command", dest="command")
argsubparsers.required = True


def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)

    if args.command == "add":
        cmd_add(args)
    elif args.command == "cat-file":
        cmd_cat_file(args)
    elif args.command == "checkout":
        cmd_checkout(args)
    elif args.command == "commit":
        cmd_commit(args)
    elif args.command == "hash-object":
        cmd_hash_object(args)
    elif args.command == "init":
        cmd_init(args)
    elif args.command == "log":
        cmd_log(args)
    elif args.command == "ls-tree":
        cmd_ls_tree(args)
    elif args.command == "merge":
        cmd_merge(args)
    elif args.command == "rebase":
        cmd_rebase(args)
    elif args.command == "rev-parse":
        cmd_rev_parse(args)
    elif args.command == "rm":
        cmd_rm(args)
    elif args.command == "show-ref":
        cmd_show_ref(args)
    elif args.command == "tag":
        cmd_tag(args)


class GitRepository:
    worktree = None
    gitdir = None
    conf_parser = None

    def __init__(self, path, force=False):
        self.worktree = path
        self.gitdir = os.path.join(path, ".git")

        if not (force or os.path.isdir(self.gitdir)):
            raise Exception("Not a Git repository {}".format(path))

        self.conf_parser = configparser.ConfigParser()
        conf = repo_file(self, "config")

        if conf and os.path.exists(conf):
            self.conf_parser.read([conf])
        elif not force:
            raise Exception("Configuration file missing")

        if not force:
            version = int(self.conf.get("core", "repositoryformatversion"))
            if version != 0 and not force:
                raise Exception("Unsupported repositoryformatversion {}".format(version))


def repo_file(repo, *path):
    return os.path.join(repo.gitdir, *path)
