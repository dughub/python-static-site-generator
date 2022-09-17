from typing import List
from pathlib import Path
import shutil


class Parser:
    extensions: List[str] = []

    @staticmethod
    def valid_extension(extension):
        return extension in Parser.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplemented()

    @staticmethod
    def read(path: Path):
        with open(path) as file:
            return file.read()

    @staticmethod
    def write(path: Path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path) as file:
            return file.write(content)

    @staticmethod
    def copy(path: Path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions: List = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)
