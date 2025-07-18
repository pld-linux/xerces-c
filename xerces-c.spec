Summary:	Xerces C++ - XML parser for C++
Summary(pl.UTF-8):	Xerces C++ - analizator składniowy XML-a dla C++
Name:		xerces-c
Version:	3.2.5
Release:	2
License:	Apache v2.0
Group:		Libraries
Source0:	https://downloads.apache.org/xerces/c/3/sources/%{name}-%{version}.tar.xz
# Source0-md5:	19431257aeb4af684c93b7a82c47dcfe
Patch0:		%{name}-iso88592.patch
Patch1:		%{name}-link.patch
URL:		https://xerces.apache.org/xerces-c/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xerces C++ - XML parser for C++.

%description -l pl.UTF-8
Xerces C++ - analizator składniowy XML-a dla C++.

%package devel
Summary:	Header files for xerces-c library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki xerces-c
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	libstdc++-devel

%description devel
Header files for xerces-c library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki xerces-c.

%package static
Summary:	Static xerces-c library
Summary(pl.UTF-8):	Statyczna biblioteka xerces-c
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static xerces-c library.

%description static -l pl.UTF-8
Statyczna biblioteka xerces-c.

%package doc
Summary:	Extensive Xerces C++ documentation
Summary(pl.UTF-8):	Obszerna dokumentacja biblioteki Xerces C++
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Extensive Xerces C++ documentation.

%description doc -l pl.UTF-8
Obszerna dokumentacja biblioteki Xerces C++.

%package examples
Summary:	Xerces C++ examples
Summary(pl.UTF-8):	Przykłady do biblioteki Xerces C++
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description examples
Xerces C++ examples.

%description examples -l pl.UTF-8
Przykłady do biblioteki Xerces C++.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-pretty-make \
	--disable-silent-rules \
%ifnarch pentium4 %{x8664} x32
	--disable-sse2
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxerces-c.la

find samples -name .deps | xargs -r rm -rf
find samples -name '*.o' -o -name .dirstamp | xargs rm -f
cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a doc/html/* $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS LICENSE NOTICE
%attr(755,root,root) %{_libdir}/libxerces-c-3.2.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxerces-c.so
%{_includedir}/xercesc
%{_pkgconfigdir}/xerces-c.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxerces-c.a

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc-%{version}

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/CreateDOMDocument
%attr(755,root,root) %{_bindir}/DOMCount
%attr(755,root,root) %{_bindir}/DOMPrint
%attr(755,root,root) %{_bindir}/EnumVal
%attr(755,root,root) %{_bindir}/MemParse
%attr(755,root,root) %{_bindir}/PParse
%attr(755,root,root) %{_bindir}/PSVIWriter
%attr(755,root,root) %{_bindir}/Redirect
%attr(755,root,root) %{_bindir}/SAX2Count
%attr(755,root,root) %{_bindir}/SAX2Print
%attr(755,root,root) %{_bindir}/SAXCount
%attr(755,root,root) %{_bindir}/SAXPrint
%attr(755,root,root) %{_bindir}/SCMPrint
%attr(755,root,root) %{_bindir}/SEnumVal
%attr(755,root,root) %{_bindir}/StdInParse
%attr(755,root,root) %{_bindir}/XInclude
%{_examplesdir}/%{name}-%{version}
