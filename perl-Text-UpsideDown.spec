%define upstream_name    Text-UpsideDown
%define upstream_version 1.22

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Flip text upside-down using Unicode
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/Text-UpsideDown-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Test::Script)
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(Capture::Tiny)
BuildRequires:	perl(Carp)
BuildRequires:	perl(English)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module exports only one function.

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
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/ud
%{_mandir}/man1/ud.1*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.100.820-2mdv2011.0
+ Revision: 657853
- rebuild for updated spec-helper

* Fri Dec 24 2010 Shlomi Fish <shlomif@mandriva.org> 1.100.820-1mdv2011.0
+ Revision: 624646
- import perl-Text-UpsideDown


