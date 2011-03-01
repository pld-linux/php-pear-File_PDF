%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	PDF
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - PDF generation using only PHP
Summary(pl.UTF-8):	%{_pearname} - generowanie PDF za pomocą samego PHP
Name:		php-pear-%{_pearname}
Version:	0.3.2
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e87fd0aba7077e24afc4e10347830137
URL:		http://pear.php.net/package/File_PDF/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Suggests:	php-pear-HTTP_Download
Obsoletes:	php-pear-File_PDF-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(HTTP/Download.*)'

%description
This package provides PDF generation using only PHP, without requiring
any external libraries.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa umożliwia generowanie dokumentów PDF za pomocą samego PHP,
bez konieczności posiadania zewnętrznych bibliotek.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
