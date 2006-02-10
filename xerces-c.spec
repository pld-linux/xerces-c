Summary:	XML parser
Summary(pl):	Analizator sk³adniowy XML-a
Name:		xerces-c
Version:	2.7.0
%define	ver	%(echo %{version} | tr . _)
Release:	0.2
License:	Apache
Group:		Applications/Publishing/XML
Source0:	http://www.apache.org/dist/xml/xerces-c/source/%{name}-src_%{ver}.tar.gz
# Source0-md5:	04169609449a8846bc1e6891c04cadf4
Patch0:		%{name}-iso88592.patch
URL:		http://xml.apache.org/
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML parser.

%description -l pl
Analizator sk³adniowy XML-a.

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
%{name} header files.

%description devel -l pl
Pliki nag³ówkowe %{name}.

%package doc
Summary:	Extensive %{name} documentation
Summary(pl):	Obszerna dokumentacja %{name}
Group:		Documentation

%description doc
Extensive %{name} documentation and examples.

%description doc -l pl
Obszerna dokumentacja oraz przyk³ady %{name}.

%prep
%setup -q -n xerces-c-src_%{ver}
%patch0 -p1

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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} -C src/xercesc install \
	XERCESCROOT=`pwd` \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt credits.txt
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files doc
%defattr(644,root,root,755)
%doc doc/html
%{_examplesdir}/%{name}-%{version}
