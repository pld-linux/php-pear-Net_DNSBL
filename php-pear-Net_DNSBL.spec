%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	DNSBL
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - DNSBL Checker
Summary(pl):	%{_pearname} - Odpytywanie DNSBL
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fcc53573625e56cf53c053678ae7ada7
URL:		http://pear.php.net/package/Net_DNSBL/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Checks if a given Host or URL is listed on an DNSBL or SURBL.

In PEAR status of this package is: %{_status}.

%description -l pl
Za pomoc± tej klasy mo¿na sprawdziæ czy dany host lub URL jest wpisany
na listy DNSBL lub SURBL.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/Tests
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
