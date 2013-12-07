%define	_class	PEAR
%define	_subclass	Command
%define	modname	%{_class}_%{_subclass}_Packaging

Summary:	Create RPM spec files from PEAR modules
Name:		php-pear-%{modname}
Version:	0.3.0
Release:	2
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/PEAR_Command_Packaging
Source0:	http://download.pear.php.net/package/PEAR_Command_Packaging-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
This command is an improved implementation of the standard PEAR "makerpm" 
command, and contains several enhancements that make it far more flexible. 
Similar functions for other external packaging mechanisms may be added at
a later date.

Enhanced features over the original PEAR "makerpm" command include:

- Ability to define a release on the command line
- Allows more advanced customisation of the generated package name
- Allows virtual Provides/Requires that differ in format from the package name
  format
- tries to intelligently distinguish between PEAR and PECL when generating
  packages

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{modname}
%{_datadir}/pear/packages/%{modname}.xml

