%define		_class		PEAR
%define		_subclass	Command
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Packaging

Summary:	%{_pearname} - Create RPM spec files from PEAR modules
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	%mkrel 1
License:	PHP License
Group:		Development/PHP
URL:            http://pear.php.net/package/PEAR_Command_Packaging
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
Patch0:		PEAR_Command_Packaging-0.1.2-mdv_conf.diff
Requires(post): php-pear-PEAR >= 1.4.10
Requires(preun): php-pear-PEAR >= 1.4.10
Requires:	php-pear-PEAR >= 1.4.10
BuildArch:	noarch
BuildRequires:	dos2unix

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

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c
%patch0 -p0

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install -d %{buildroot}%{_datadir}/pear/data/%{_class}_%{_subclass}_Packaging

install -m0644 %{_pearname}-%{version}/Packaging.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/
install -m0644 %{_pearname}-%{version}/Packaging.xml %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/
install %{_pearname}-%{version}/template.spec %{buildroot}%{_datadir}/pear/data/%{_class}_%{_subclass}_Packaging/template.spec

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_datadir}/pear/%{_class}/%{_subclass}
%dir %{_datadir}/pear/data/%{_class}_%{_subclass}_Packaging
%{_datadir}/pear/%{_class}/%{_subclass}/Packaging.php
%{_datadir}/pear/%{_class}/%{_subclass}/Packaging.xml
%{_datadir}/pear/data/%{_class}_%{_subclass}_Packaging/template.spec
%{_datadir}/pear/packages/%{_pearname}.xml


