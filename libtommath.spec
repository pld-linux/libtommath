Summary:	LibTomMath - routines for integer based number theoretic applications
Summary(pl.UTF-8):   LibTomMath - procedury do zastosowań teorii liczb z zakresu liczb całkowitych
Name:		libtommath
Version:	0.39
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://math.libtomcrypt.com/files/ltm-%{version}.tar.bz2
# Source0-md5:	5f3c9287a6d65e2c3f6d47ad60797aeb
URL:		http://math.libtomcrypt.com/
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
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
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki LibTomMath
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LibTomMath library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LibTomMath.

%package static
Summary:	Static LibTomMath library
Summary(pl.UTF-8):   Statyczna biblioteka LibTomMath
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LibTomMath library.

%description static -l pl.UTF-8
Statyczna biblioteka LibTomMath.

%prep
%setup -q

sed -i -e 's/\<gcc\>/$(GCC)/' makefile.shared

%build
%{__make} -f makefile.shared \
	GCC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I. -Wall -W -Wshadow -Wsign-compare" \
	LIBPATH=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -f makefile.shared install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBPATH=%{_libdir} \
	INSTALL_GROUP="`id -g`" \
	INSTALL_USER="`id -u`"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/libtommath.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc bn.pdf tommath.pdf
%attr(755,root,root) %{_libdir}/libtommath.so
%{_libdir}/libtommath.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libtommath.a
