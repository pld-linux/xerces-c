Summary:	XML parser
Summary(pl):	Parser XML
Name:		xerces-c
Version:	1.7.0
%define	ver	%(echo %{version} | tr . _)
Release:	1
License:	Apache Software License
Group:		Applications/Publishing/XML
Source0:	http://xml.apache.org/dist/xerces-c/stable/%{name}-src%{ver}.tar.gz
Patch0:		%{name}-opt.patch
URL:		http://xml.apache.org/
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML parser.

%description -l pl
Parser XML.

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
%{name} header files and documentation

%description devel -l pl
Pliki nag³ówkowe i dokumentacja %{name}.

%prep
%setup -q -n xerces-c-src%{ver}
%patch -p1

%build
## What a shit!!!
XERCESCROOT=`pwd`; export XERCESCROOT
cd src/xercesc
%{__autoconf}
chmod 755 runConfigure
./runConfigure -plinux -cgcc -xg++ -minmem -nsocket -tnative -rpthread \
	-z%(echo %{rpmcflags} | sed -e 's/\(.\) \+\(.\)/\1 -z\2/g')

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_examplesdir}/%{name}-%{version}}

# Only one file?
install lib/lib*.so $RPM_BUILD_ROOT%{_libdir}

# I put all stuff from that dir, maybe some can be omitted
cp -a include/xercesc $RPM_BUILD_ROOT%{_includedir}

cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt credits.txt
%attr(755,root,root) %{_libdir}/lib*.so

%files devel
%defattr(644,root,root,755)
%doc doc/html
%{_includedir}/*
%{_examplesdir}/%{name}-%{version}
