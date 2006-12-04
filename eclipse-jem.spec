%define		_buildid	200609261748
Summary:	Java EMF Model
Name:		eclipse-jem
Version:	1.2.1
Release:	0.1
License:	CPL
Group:		Development/Tools
Source0:	http://download.eclipse.org/tools/ve/downloads/drops/R-%{version}-%{_buildid}/JEM-SDK-%{version}.zip
# Source0-md5:	2ee5413d360c62e74bef4826024a80ad
#URL:		
BuildRequires:	unzip
Requires:	eclipse >= 3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_eclipsedir	%{_datadir}/eclipse

%description
Java EMF Model, including BeanInfo, Java Model, Proxy support
(with remote vm and IDE vm support).

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}
cp -rf eclipse/features/* $RPM_BUILD_ROOT%{_eclipsedir}/features
cp -rf eclipse/plugins/* $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/org.eclipse.jem*
%{_eclipsedir}/plugins/org.eclipse.jem*
%{_eclipsedir}/plugins/com.ibm.etools.emf*
