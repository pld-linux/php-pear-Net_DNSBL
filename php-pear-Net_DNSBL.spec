%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	DNSBL
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - DNSBL Checker
Summary(pl):	%{_pearname} - Odpytywanie DNSBL
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fcc53573625e56cf53c053678ae7ada7
URL:		http://pear.php.net/package/Net_DNSBL/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.3.6
Requires:	php-pear
Requires:	php-pear-Cache_Lite >= 1.3.1
Requires:	php-pear-Net_CheckIP >= 1.1
Requires:	php-pear-HTTP_Request >= 1.2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Checks if a given Host or URL is listed on an DNSBL or SURBL.

In PEAR status of this package is: %{_status}.

%description -l pl
Za pomoc± tej klasy mo¿na sprawdziæ czy dany host lub URL jest wpisany
na listy DNSBL lub SURBL.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
