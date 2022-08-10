#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Parallel-Iterator
Version  : 1.002
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/Parallel-Iterator-1.002.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/Parallel-Iterator-1.002.tar.gz
Summary  : 'Simple parallel execution'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Parallel-Iterator-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Parallel::Iterator
This module provides a 'parallel map'. Multiple worker processes are
forked so that many instances of the transformation function may be
executed simultaneously.

%package dev
Summary: dev components for the perl-Parallel-Iterator package.
Group: Development
Provides: perl-Parallel-Iterator-devel = %{version}-%{release}
Requires: perl-Parallel-Iterator = %{version}-%{release}

%description dev
dev components for the perl-Parallel-Iterator package.


%package perl
Summary: perl components for the perl-Parallel-Iterator package.
Group: Default
Requires: perl-Parallel-Iterator = %{version}-%{release}

%description perl
perl components for the perl-Parallel-Iterator package.


%prep
%setup -q -n Parallel-Iterator-1.002
cd %{_builddir}/Parallel-Iterator-1.002

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Parallel::Iterator.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
