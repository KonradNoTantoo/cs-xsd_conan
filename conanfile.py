from conans import ConanFile, tools
import os


class CSXsdConan(ConanFile):
    name = "cs-xsd"
    version = "4.0.0"
    license = "GPLv2"
    author = "konrad.no.tantoo"
    url = "https://github.com/KonradNoTantoo/cs-xsd_conan"
    description = "CodeSynthesis XSD is an open-source, cross-platform W3C XML Schema to C++ data binding compiler."
    topics = ("XML", "XSD", "data binding")
    settings = "os", "arch"
    options = { "nename_executable": [True, False] }
    default_options = { "nename_executable": True }
    requires = "xerces-c/3.2.2@bincrafters/stable"
    no_copy_source = True
    _source_subfolder = "source_subfolder"


    def configure(self):
        if self.settings.os == "Windows":
            del self.settings.arch


    def source(self):
        # not a mistake, we want to test os, not compiler
        if self.settings.os == "Windows":
            extracted_dir = "xsd-{}-i686-windows".format(self.version)
            dl_path = "https://www.codesynthesis.com/download/xsd/4.0/windows/i686/{}.zip".format(extracted_dir)
        elif self.settings.os == "Linux":
            if self.settings.arch == "x86_64":
                extracted_dir = "xsd-{}-x86_64-linux-gnu".format(self.version)
                dl_path = "https://www.codesynthesis.com/download/xsd/4.0/linux-gnu/x86_64/{}.tar.bz2".format(extracted_dir)
            elif self.settings.arch == "x86":
                extracted_dir = "xsd-{}-i686-linux-gnu".format(self.version)
                dl_path = "https://www.codesynthesis.com/download/xsd/4.0/linux-gnu/i686/{}.tar.bz2".format(extracted_dir)
        # elif self.settings.os == "Mac OS X":
        # elif self.settings.os == "Solaris":
        else:
            raise conans.errors.ConanException("OS {} not supported".format(self.settings.os))

        tools.get(dl_path)
        os.rename(extracted_dir, self._source_subfolder)

        if self.options.nename_executable:
            # rename executable to cs-xsd to avoid collision with
            # MS Xml Schemas/DataTypes support utility who is also
            # named xsd.exe
            bin_name = "xsd.exe" if self.settings.os == "Windows" else "xsd"
            bin_path = os.path.join(self._source_subfolder, "bin")
            old_executable = os.path.join(bin_path, bin_name)
            new_executable = os.path.join(bin_path, "cs-{}".format(bin_name))
            self.output.info("Renaming {} to {}".format(old_executable, new_executable))
            os.rename(old_executable, new_executable)


    def package(self):
        libxsd_path = os.path.join(self._source_subfolder, "libxsd")
        self.copy("*.?xx", dst="include", src=libxsd_path, keep_path=True)
        if self.options.nename_executable:
            self.copy("bin/cs-xsd*", dst="bin", src=self._source_subfolder, keep_path=False)
        else:
            self.copy("bin/xsd*", dst="bin", src=self._source_subfolder, keep_path=False)


    def package_info(self):
        bindir = os.path.join(self.package_folder, "bin")
        self.output.info("Appending PATH environment variable: {}".format(bindir))
        self.env_info.PATH.append(bindir)


    def package_id(self):
        if self.info.settings.os == "Windows":
            del self.info.settings.arch
