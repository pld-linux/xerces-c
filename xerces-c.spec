%define	ver	%(echo %{version} | tr . _)
Summary:	XML parser
Summary(pl.UTF-8):	Analizator składniowy XML-a
Name:		xerces-c
Version:	2.8.0
Release:	2
License:	Apache
Group:		Applications/Publishing/XML
Source0:	http://www.apache.org/dist/xerces/c/sources/%{name}-src_%{ver}.tar.gz
# Source0-md5:	5daf514b73f3e0de9e3fce704387c0d2
Patch0:		%{name}-iso88592.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-opt.patch
Patch3:		%{name}-lib64.patch
URL:		http://xml.apache.org/
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML parser.

%description -l pl.UTF-8
Analizator składniowy XML-a.

%package devel
Summary:	%{name} header files
Summary(pl.UTF-8):	Pliki nagłówkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
%{name} header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe %{name}.

%package doc
Summary:	Extensive %{name} documentation
Summary(pl.UTF-8):	Obszerna dokumentacja %{name}
Group:		Documentation

%description doc
Extensive %{name} documentation and examples.

%description doc -l pl.UTF-8
Obszerna dokumentacja oraz przykłady %{name}.

%prep
%setup -q -n %{name}-src_%{ver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%ifarch %{x8664}
%patch3 -p1
%endif

%build
## What a shit!!!
XERCESCROOT=`pwd`; export XERCESCROOT
cd src/xercesc
%{__autoconf}
chmod 755 runConfigure
./runConfigure -plinux -cgcc -xg++ -minmem -nsocket -tnative -rpthread \
	-z%(echo %{rpmcflags} | sed -e 's/\(.\) \+\(.\)/\1 -z\2/g')

%{__make} -j1

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
