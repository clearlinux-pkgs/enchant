#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : enchant
Version  : 2.3.0
Release  : 17
URL      : https://github.com/AbiWord/enchant/releases/download/v2.3.0/enchant-2.3.0.tar.gz
Source0  : https://github.com/AbiWord/enchant/releases/download/v2.3.0/enchant-2.3.0.tar.gz
Summary  : A spell checking library
Group    : Development/Tools
License  : LGPL-2.1
Requires: enchant-bin = %{version}-%{release}
Requires: enchant-data = %{version}-%{release}
Requires: enchant-lib = %{version}-%{release}
Requires: enchant-license = %{version}-%{release}
Requires: enchant-man = %{version}-%{release}
BuildRequires : aspell-dev
BuildRequires : hunspell-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)

%description
libenchant -- Generic spell checking library
Maintainer: Reuben Thomas
Home page: https://abiword.github.io/enchant/

%package bin
Summary: bin components for the enchant package.
Group: Binaries
Requires: enchant-data = %{version}-%{release}
Requires: enchant-license = %{version}-%{release}

%description bin
bin components for the enchant package.


%package data
Summary: data components for the enchant package.
Group: Data

%description data
data components for the enchant package.


%package dev
Summary: dev components for the enchant package.
Group: Development
Requires: enchant-lib = %{version}-%{release}
Requires: enchant-bin = %{version}-%{release}
Requires: enchant-data = %{version}-%{release}
Provides: enchant-devel = %{version}-%{release}
Requires: enchant = %{version}-%{release}

%description dev
dev components for the enchant package.


%package lib
Summary: lib components for the enchant package.
Group: Libraries
Requires: enchant-data = %{version}-%{release}
Requires: enchant-license = %{version}-%{release}

%description lib
lib components for the enchant package.


%package license
Summary: license components for the enchant package.
Group: Default

%description license
license components for the enchant package.


%package man
Summary: man components for the enchant package.
Group: Default

%description man
man components for the enchant package.


%prep
%setup -q -n enchant-2.3.0
cd %{_builddir}/enchant-2.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623858419
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1623858419
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/enchant
cp %{_builddir}/enchant-2.3.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/enchant/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/enchant-2
/usr/bin/enchant-lsmod-2

%files data
%defattr(-,root,root,-)
/usr/share/enchant/enchant.ordering

%files dev
%defattr(-,root,root,-)
/usr/include/enchant-2/enchant++.h
/usr/include/enchant-2/enchant-provider.h
/usr/include/enchant-2/enchant.h
/usr/lib64/libenchant-2.so
/usr/lib64/pkgconfig/enchant-2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/enchant-2/enchant_aspell.so
/usr/lib64/enchant-2/enchant_hunspell.so
/usr/lib64/libenchant-2.so.2
/usr/lib64/libenchant-2.so.2.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/enchant/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/enchant-2.1
/usr/share/man/man1/enchant-lsmod-2.1
