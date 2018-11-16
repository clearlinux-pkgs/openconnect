#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x63762CDA67E2F359 (dwmw2@exim.org)
#
Name     : openconnect
Version  : 7.08
Release  : 19
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
Requires: openconnect-data
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : krb5-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(libproxy-1.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(p11-kit-1)
BuildRequires : pkgconfig(zlib)

Patch1: 0001-Include-the-vpnc-script-directly-into-the-build.patch

%description
Description:
This directory contains a JNI interface layer for libopenconnect, and a
demo program to show how it can be used.

%package bin
Summary: bin components for the openconnect package.
Group: Binaries
Requires: openconnect-data

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
Requires: openconnect-lib
Requires: openconnect-bin
Requires: openconnect-data
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
Requires: openconnect-data

%description lib
lib components for the openconnect package.


%package locales
Summary: locales components for the openconnect package.
Group: Default

%description locales
locales components for the openconnect package.


%prep
%setup -q -n openconnect-7.08
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507490916
%reconfigure --disable-static --with-vpnc-script=/usr/share/vpnc/vpnc-script
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507490916
rm -rf %{buildroot}
%make_install
%find_lang openconnect

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/openconnect

%files data
%defattr(-,root,root,-)
/usr/share/vpnc/vpnc-script

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

