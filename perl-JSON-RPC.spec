%define upstream_name    JSON-RPC
%define upstream_version 0.96

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	JSON-RPC sever for mod_perl2
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/JSON/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(JSON)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module is a smple code (for Perl 5.6 or later). Please check the
source.

PROCEDURES
    * echo

      Takes a scalar and returns it as is.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.960.0-2mdv2011.0
+ Revision: 657783
- rebuild for updated spec-helper

* Fri Oct 22 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.960.0-1mdv2011.0
+ Revision: 587225
- import perl-JSON-RPC

