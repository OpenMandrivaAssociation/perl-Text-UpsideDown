%define upstream_name    Text-UpsideDown
%define upstream_version 1.100820

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Flip text upside-down using Unicode
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module exports only one function.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%perl_vendorlib/*


