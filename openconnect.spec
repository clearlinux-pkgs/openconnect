#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x63762CDA67E2F359 (dwmw2@exim.org)
#
Name     : openconnect
Version  : 7.08
Release  : 12
URL      : ftp://ftp.infradead.org/pub/openconnect/openconnect-7.08.tar.gz
Source0  : ftp://ftp.infradead.org/pub/openconnect/openconnect-7.08.tar.gz
Source99 : ftp://ftp.infradead.org/pub/openconnect/openconnect-7.08.tar.gz.asc
Summary  : OpenConnect VPN client
Group    : Development/Tools
License  : LGPL-2.1
Requires: openconnect-bin
Requires: openconnect-lib
Requires: openconnect-locales
Requires: openconnect-doc
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(p11-kit-1)
BuildRequires : pkgconfig(zlib)
BuildRequires : python-dev

%description
Description:
This directory contains a JNI interface layer for libopenconnect, and a
demo program to show how it can be used.

%package bin
Summary: bin components for the openconnect package.
Group: Binaries

%description bin
bin components for the openconnect package.


%package dev
Summary: dev components for the openconnect package.
Group: Development
Requires: openconnect-lib
Requires: openconnect-bin
Provides: openconnect-devel

%description dev
dev components for the openconnect package.


%package doc
Summary: doc components for the openconnect package.
Group: Documentation

%description doc
doc components for the openconnect package.


%package lib
Summary: lib components for the openconnect package.
Group: Libraries

%description lib
lib components for the openconnect package.


%package locales
Summary: locales components for the openconnect package.
Group: Default

%description locales
locales components for the openconnect package.


%prep
%setup -q -n openconnect-7.08

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492436646
%configure --disable-static --with-vpnc-script==/usr/share/vpnc/vpnc-script
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1492436646
rm -rf %{buildroot}
%make_install
%find_lang openconnect

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/openconnect

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libopenconnect.so
/usr/lib64/pkgconfig/openconnect.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libopenconnect.so.5
/usr/lib64/libopenconnect.so.5.4.0

%files locales -f openconnect.lang
%defattr(-,root,root,-)

