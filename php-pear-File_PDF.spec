%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	PDF
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - PDF generation using only PHP
Summary(pl):	%{_pearname} - generowanie PDF za pomoc± samego PHP
Name:		php-pear-%{_pearname}
Version:	0.0.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d912b734c33adba85ccc0f52a6eee98a
URL:		http://pear.php.net/package/File_PDF/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides PDF generation using only PHP, without requiring
any external libraries.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa umo¿liwia generowanie dokumentów PDF za pomoc± samego PHP, bez
konieczno¶ci posiadania zewnêtrznych bibliotek.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/fonts

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/fonts/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/fonts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
