%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	DNSBL
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - DNSBL Checker
Summary(pl):	%{_pearname} - Odpytywanie DNSBL
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	bf9a88934459b6b5da7e5b09a8f6e342
URL:		http://pear.php.net/package/Net_DNSBL/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3.11
Requires:	php-pear
Requires:	php-pear-Cache_Lite >= 1.4.1
Requires:	php-pear-HTTP_Request >= 1.2.3
Requires:	php-pear-Net_CheckIP >= 1.1
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
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests
rm -rf .%{php_pear_dir}/tests/Net_DNSBL/Tests

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
