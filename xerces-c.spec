Summary:	XML parser
Summary(pl):	Parser XML
Name:		xerces-c
Version:	1.2.0a
%define	ver	1_2_0a
%define	mainver	1_2_0
Release:	1
License:	GPL
Group:		Applications/Publishing/XML
Group(pl):	Aplikacje/Publikowanie/XML
Source0:	http://xml.apache.org/dist/xerces-c/stable/Xerces-C-src_%{ver}.tar.gz
URL:		http://xml.apache.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
%{name} header files and documentation

%description -l pl devel
Pliki nag³ówkowe i dokumentacja %{name}.

%prep
%setup -q -n xerces-c-src_%{mainver}/src

%build
#chmod 755 configure config.{guess,status,sub}

## What a shit!!!

export XERCESCROOT=`cd .. ; pwd`
autoconf
chmod 755 runConfigure
./runConfigure -plinux -cgcc -xg++ -minmem -nfileonly -tnative
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_libdir}
install -d $RPM_BUILD_ROOT/%{_includedir}

# Only one file?
cp -a ../lib/* $RPM_BUILD_ROOT%{_libdir}

# I put all stuff from that dir, maybe some can be omitted
cp -a ../include/* $RPM_BUILD_ROOT%{_includedir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*

%files devel
%defattr(644,root,root,755)
%doc ../doc/html ../samples
%{_includedir}/*
##%{_libdir}/*.so
