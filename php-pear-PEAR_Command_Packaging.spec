%define		_class		PEAR
%define		_subclass	Command
%define		upstream_name	%{_class}_%{_subclass}_Packaging

Name:		php-pear-%{upstream_name}
Version:	0.3.0
Release:	1
Summary:	Create RPM spec files from PEAR modules
License:	PHP License
Group:		Development/PHP
URL:        http://pear.php.net/package/PEAR_Command_Packaging
Source0:	http://download.pear.php.net/package/PEAR_Command_Packaging-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

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
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-5mdv2011.0
+ Revision: 667636
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-4mdv2011.0
+ Revision: 607130
- rebuild

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-3mdv2010.1
+ Revision: 467943
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Oct 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-2mdv2010.0
+ Revision: 452037
- fix %%postun

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1mdv2010.0
+ Revision: 450270
- new version
- use pear installer
- use fedora %%post/%%postun

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1.2-5mdv2010.0
+ Revision: 426664
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-4mdv2009.1
+ Revision: 321891
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-3mdv2009.0
+ Revision: 224841
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-2mdv2008.1
+ Revision: 178533
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-1mdv2007.0
+ Revision: 81184
- Import php-pear-PEAR_Command_Packaging

* Wed Aug 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-1mdk
- initial Mandriva package (fixes #24033)


