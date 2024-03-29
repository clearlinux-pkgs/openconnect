#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0x63762CDA67E2F359 (dwmw2@exim.org)
#
Name     : openconnect
Version  : 9.12
Release  : 37
URL      : https://www.infradead.org/openconnect/download/openconnect-9.12.tar.gz
Source0  : https://www.infradead.org/openconnect/download/openconnect-9.12.tar.gz
Source1  : https://www.infradead.org/openconnect/download/openconnect-9.12.tar.gz.asc
Summary  : OpenConnect VPN client
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: openconnect-bin = %{version}-%{release}
Requires: openconnect-data = %{version}-%{release}
Requires: openconnect-lib = %{version}-%{release}
Requires: openconnect-libexec = %{version}-%{release}
Requires: openconnect-license = %{version}-%{release}
Requires: openconnect-locales = %{version}-%{release}
Requires: openconnect-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gmp-dev
BuildRequires : json-glib-dev
BuildRequires : krb5-dev
BuildRequires : perl(Getopt::Long)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(hogweed)
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(libproxy-1.0)
BuildRequires : pkgconfig(libtasn1)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(p11-kit-1)
BuildRequires : pkgconfig(stoken)
BuildRequires : pkgconfig(tss2-esys)
BuildRequires : pkgconfig(tss2-mu)
BuildRequires : pkgconfig(tss2-tctildr)
BuildRequires : pkgconfig(zlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Include-the-vpnc-script-directly-into-the-build.patch

%description
Description:
This directory contains a JNI interface layer for libopenconnect, and a
demo program to show how it can be used.

%package bin
Summary: bin components for the openconnect package.
Group: Binaries
Requires: openconnect-data = %{version}-%{release}
Requires: openconnect-libexec = %{version}-%{release}
Requires: openconnect-license = %{version}-%{release}

%description bin
bin components for the openconnect package.


%package data
Summary: data components for the openconnect package.
Group: Data

%description data
data components for the openconnect package.


%package dev
Summary: dev components for the openconnect package.
Group: Development
Requires: openconnect-lib = %{version}-%{release}
Requires: openconnect-bin = %{version}-%{release}
Requires: openconnect-data = %{version}-%{release}
Provides: openconnect-devel = %{version}-%{release}
Requires: openconnect = %{version}-%{release}

%description dev
dev components for the openconnect package.


%package lib
Summary: lib components for the openconnect package.
Group: Libraries
Requires: openconnect-data = %{version}-%{release}
Requires: openconnect-libexec = %{version}-%{release}
Requires: openconnect-license = %{version}-%{release}

%description lib
lib components for the openconnect package.


%package libexec
Summary: libexec components for the openconnect package.
Group: Default
Requires: openconnect-license = %{version}-%{release}

%description libexec
libexec components for the openconnect package.


%package license
Summary: license components for the openconnect package.
Group: Default

%description license
license components for the openconnect package.


%package locales
Summary: locales components for the openconnect package.
Group: Default

%description locales
locales components for the openconnect package.


%package man
Summary: man components for the openconnect package.
Group: Default

%description man
man components for the openconnect package.


%prep
%setup -q -n openconnect-9.12
cd %{_builddir}/openconnect-9.12
%patch -P 1 -p1
pushd ..
cp -a openconnect-9.12 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702042104
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%reconfigure --disable-static --with-vpnc-script=/usr/share/vpnc/vpnc-script
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
%reconfigure --disable-static --with-vpnc-script=/usr/share/vpnc/vpnc-script
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702042104
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openconnect
cp %{_builddir}/openconnect-%{version}/COPYING.LGPL %{buildroot}/usr/share/package-licenses/openconnect/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/openconnect-%{version}/www/licence.xml %{buildroot}/usr/share/package-licenses/openconnect/ca4f3956feba7bf35cee18cef7f157f4a732e869 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang openconnect
## Remove excluded files
rm -f %{buildroot}*/usr/libexec/openconnect/hipreport-android.sh
rm -f %{buildroot}*/usr/libexec/openconnect/tncc-wrapper.py
rm -f %{buildroot}*/usr/libexec/openconnect/tncc-emulate.py
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/openconnect
/usr/bin/openconnect

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/openconnect
/usr/share/vpnc/vpnc-script

%files dev
%defattr(-,root,root,-)
/usr/include/openconnect.h
/usr/lib64/libopenconnect.so
/usr/lib64/pkgconfig/openconnect.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libopenconnect.so.5.9.0
/usr/lib64/libopenconnect.so.5
/usr/lib64/libopenconnect.so.5.9.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/openconnect/csd-post.sh
/usr/libexec/openconnect/csd-wrapper.sh
/usr/libexec/openconnect/hipreport.sh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openconnect/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/openconnect/ca4f3956feba7bf35cee18cef7f157f4a732e869

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/openconnect.8

%files locales -f openconnect.lang
%defattr(-,root,root,-)

