Summary:	Create an index of scalable font files for X
Name:		mkfontscale
Version:	1.1.2
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
# add a few extra encodings
Patch0:		mkfontscale-1.0.3-mdv.patch
Patch2:		mkfontscale-1.1.0-linkage.patch

BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(fontenc)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)

%description
For each directory argument, mkfontscale reads all of the scalable font files
in the directory. For every font file found, an X11 font name (XLFD) is
generated, and is written together with the file name to a file fonts.scale in
the directory.

%prep
%setup -q
%apply_patches

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/mkfontscale
%{_mandir}/man1/mkfontscale.*
