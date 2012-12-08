Name:		mkfontscale
Version:	1.1.0
Release:	2
Summary:	Create an index of scalable font files for X
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
# add a few extra encodings
Patch0:		mkfontscale-1.0.3-mdv.patch

BuildRequires:	pkgconfig(fontenc)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	x11-util-macros

%description
For each directory argument, mkfontscale reads all of the scalable font files
in the directory. For every font file found, an X11 font name (XLFD) is
generated, and is written together with the file name to a file fonts.scale in
the directory.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/mkfontscale
%{_mandir}/man1/mkfontscale.*

