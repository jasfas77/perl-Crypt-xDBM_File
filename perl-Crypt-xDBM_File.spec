#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	xDBM_File
Summary:	Crypt::xDBM_File Perl module - encrypt almost any kind of dbm file
Summary(pl):	Modu� Perla Crypt::xDBM_File - szyfrowanie prawie wszystkich rodzaj�w plik�w dbm
Name:		perl-Crypt-xDBM_File
Version:	1.01
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4e1c91ebbf896ae094c7b150e4c67883
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-DES
BuildRequires:	perl-Crypt-IDEA
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::xDBM_File encrypts/decrypts the data in a gdbm, ndbm, sdbm (and
maybe even BerkeleyDB, but it wasn't tested by the author) file. It
gets tied to a hash and you just access the hash like normal. The
crypt function can be any of the CPAN modules that use encrypt,
decrypt, keysize, blocksize (so Crypt::IDEA, Crypt::DES,
Crypt::Blowfish... should all work).

%description -l pl
Modu� Crypt::xDBM_File szyfruje i deszyfruje dane w plikach gdbm,
ndbm, sdbm (by� mo�e tak�e BerkeleyDB, ale nie by�o to testowane przez
autora). Modu� przywi�zuje si� do hasza, do kt�rego mo�na potem
odwo�ywa� si� w normalny spos�b. Funkcj� szyfruj�ca mo�e by� dowolny z
modu��w CPAN u�ywaj�cy funkcji encrypt, decrypt, keysize, blocksize
(czyli modu�y Crypt::IDEA, Crypt::DES, Crypt::Blowfish... powinny
wszystkie dzia�a�).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Crypt/xDBM_File.pm
%{_mandir}/man3/*
