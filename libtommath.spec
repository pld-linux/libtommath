Summary:	LibTomMath - routines for integer based number theoretic applications
Summary(pl.UTF-8):	LibTomMath - procedury do zastosowań teorii liczb z zakresu liczb całkowitych
Name:		libtommath
Version:	1.3.0
Release:	1
License:	Public Domain or WTFPL v2
Group:		Libraries
#Source0Download: https://github.com/libtom/libtommath/releases
Source0:	https://github.com/libtom/libtommath/releases/download/v%{version}/ltm-%{version}.tar.xz
# Source0-md5:	59d7440e1f60719a1d3cc8c4f1df2d6b
Patch0:		%{name}-pc.patch
URL:		http://www.libtom.net/LibTomMath/
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
LibTomMath provides highly optimized and portable routines for a vast
majority of integer based number theoretic applications (including
public key cryptography). LibTomMath is not a cryptographic toolkit
itself but it can be used to write one (is used in LibTomCrypt for
RSA, DH and ECC public key routines).

%description -l pl.UTF-8
LibTomMath zawiera wysoko zoptymalizowane i przenośne procedury do
większości zastosowań teorii liczb z zakresu liczb całkowitych
(włącznie z kryptografią klucza publicznego). LibTomMath jako taka
nie jest zestawem procedur kryptograficznych, ale może być użyta do
napisania takowego (jest używana w LibTomCrypt do procedur klucza
publicznego RSA, DH i ECC).

%package devel
Summary:	Header files for LibTomMath library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LibTomMath
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LibTomMath library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LibTomMath.

%package static
Summary:	Static LibTomMath library
Summary(pl.UTF-8):	Statyczna biblioteka LibTomMath
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LibTomMath library.

%description static -l pl.UTF-8
Statyczna biblioteka LibTomMath.

%prep
%setup -q
%patch0 -p1

%build
# IGNORE_SPEED avoids overriding rpmcflags
CFLAGS="%{rpmcflags}" \
%{__make} -f makefile.shared \
	CC="%{__cc}" \
	IGNORE_SPEED=1 \
	LIBPATH=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -f makefile.shared install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBPATH=%{_libdir}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtommath.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md changes.txt
%attr(755,root,root) %{_libdir}/libtommath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtommath.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/bn.pdf
%attr(755,root,root) %{_libdir}/libtommath.so
%{_includedir}/tommath*.h
%{_pkgconfigdir}/libtommath.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtommath.a
