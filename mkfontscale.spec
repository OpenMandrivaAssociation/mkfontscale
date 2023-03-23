Summary:	Create an index of scalable font files for X
Name:		mkfontscale
Version:	1.2.2
Release:	3
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
# add a few extra encodings
Patch0:		https://src.fedoraproject.org/rpms/mkfontscale/raw/rawhide/f/mkfontscale-examine-all-encodings.patch
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(fontenc)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)
%rename mkfontdir
Requires:	/bin/sh

%description
For each directory argument, mkfontscale reads all of the scalable font files
in the directory. For every font file found, an X11 font name (XLFD) is
generated, and is written together with the file name to a file fonts.scale in
the directory.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/mk*
%doc %{_mandir}/man1/mk*.*
