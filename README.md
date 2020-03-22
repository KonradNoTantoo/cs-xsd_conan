# Conan recipe for CodeSynthesis XSD data-binder 4.0.0

[![Build Status: Windows](https://ci.appveyor.com/api/projects/status/github/KonradNoTantoo/cs-xsd_conan?svg=true)](https://ci.appveyor.com/project/KonradNoTantoo/cx_xsd-conan)

[![Build Status: Linux](https://api.travis-ci.org/KonradNoTantoo/cs-xsd_conan.svg?branch=master)](https://travis-ci.org/KonradNoTantoo/cs-xsd_conan)

### Description
Conan recipe that installs pre-built binaries and headers for [CodeSynthesis XSD](https://www.codesynthesis.com/projects/xsd/).

By default, packaged executable is renamed from xsd to cs-xsd in order to prevent name collision with xsd executable used by Microsoft .NET and Mono. This renaming can be disabled by setting cs-xsd:rename_executable conan option to False.

### Repository
Published on [Utopia bintray](https://bintray.com/konradnotantoo/utopia/):
```
conan remote add utopia https://api.bintray.com/conan/konradnotantoo/utopia
```

### Recipe license
MIT