#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yelp-tools
Version  : 3.28.0
Release  : 6
URL      : https://download.gnome.org/sources/yelp-tools/3.28/yelp-tools-3.28.0.tar.xz
Source0  : https://download.gnome.org/sources/yelp-tools/3.28/yelp-tools-3.28.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: yelp-tools-bin
Requires: yelp-tools-data
BuildRequires : itstool
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(yelp-xsl)

%description
ABOUT
=====
yelp-tools is a collection of scripts and build utilities to help create,
manage, and publish documentation for Yelp and the web. Most of the heavy
lifting is done by packages like yelp-xsl and itstool. This package just
wraps things up in a developer-friendly way.

%package bin
Summary: bin components for the yelp-tools package.
Group: Binaries
Requires: yelp-tools-data

%description bin
bin components for the yelp-tools package.


%package data
Summary: data components for the yelp-tools package.
Group: Data

%description data
data components for the yelp-tools package.


%package dev
Summary: dev components for the yelp-tools package.
Group: Development
Requires: yelp-tools-bin
Requires: yelp-tools-data
Provides: yelp-tools-devel

%description dev
dev components for the yelp-tools package.


%prep
%setup -q -n yelp-tools-3.28.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526271175
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1526271175
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/yelp-build
/usr/bin/yelp-check
/usr/bin/yelp-new

%files data
%defattr(-,root,root,-)
/usr/share/yelp-tools/templates/task.page
/usr/share/yelp-tools/xslt/comments.xsl
/usr/share/yelp-tools/xslt/mal-epub.xsl
/usr/share/yelp-tools/xslt/mal-files.xsl
/usr/share/yelp-tools/xslt/mal-license.xsl
/usr/share/yelp-tools/xslt/mal-ncx.xsl
/usr/share/yelp-tools/xslt/mal-opf.xsl
/usr/share/yelp-tools/xslt/mal-rng.xsl
/usr/share/yelp-tools/xslt/mal-status.xsl
/usr/share/yelp-tools/xslt/media.xsl

%files dev
%defattr(-,root,root,-)
/usr/share/aclocal/*.m4
