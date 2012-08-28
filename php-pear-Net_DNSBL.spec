%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Net_DNSBL
Summary:	%{_pearname} - DNSBL Checker
Summary(pl.UTF-8):	%{_pearname} - Odpytywanie DNSBL
Name:		php-pear-%{_pearname}
Version:	1.3.7
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6e15d7802ea8dfa61acc2691411ac29b
URL:		http://pear.php.net/package/Net_DNSBL/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.3.11
Requires:	php-pear
Requires:	php-pear-Net_CheckIP >= 1.1
Requires:	php-pear-Net_DNS >= 1.0.0
Requires:	php-pear-PEAR-core >= 1:1.4.0
# should be suggests, not requires: http://pear.php.net/bugs/bug.php?id=17789
Suggests:	php-pear-Cache_Lite >= 1.4.1
Suggests:	php-pear-HTTP_Request2 >= 2.0.0
Obsoletes:	php-pear-Net_DNSBL-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Cache/Lite.php) pear(HTTP/Request.php)

%description
Checks if a given Host or URL is listed on an DNSBL or SURBL.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Za pomocą tej klasy można sprawdzić czy dany host lub URL jest wpisany
na listy DNSBL lub SURBL.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# phing build file
rm .%{php_pear_dir}/data/Net_DNSBL/build.xml

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
%{php_pear_dir}/Net/DNSBL.php
%{php_pear_dir}/Net/DNSBL
