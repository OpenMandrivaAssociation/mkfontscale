Name: mkfontscale
Version: 1.0.3
Release: %mkrel 3
Summary: Create an index of scalable font files for X
Group: Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/app/mkfontscale xorg/app/mkfontscale
# cd xorg/app/showfont
# git-archive --format=tar --prefix=mkfontscale-1.0.3/ mkfontscale-1.0.3 | bzip2 -9 > mkfontscale-1.0.3.tar.bz2
########################################################################
Source: %{name}-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch mkfontscale-1.0.3..origin/mandriva+custom
Patch1: 0001-Rename-.cvsignore-to-.gitignore.patch
Patch2: 0002-Add-to-.gitignore-to-skip-patch-emacs-droppings.patch
Patch3: 0003-extra-encodings-used-by-some-legacy-Mandriva-locale.patch
########################################################################
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: zlib-devel
BuildRequires: x11-proto-devel	>= 7.3
BuildRequires: freetype2-devel	>= 2.3.5
BuildRequires: libfontenc-devel >= 1.0.1

%description
For each directory argument, mkfontscale reads all of the scalable font files
in the directory. For every font file found, an X11 font name (XLFD) is
generated, and is written together with the file name to a file fonts.scale in
the directory.

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/mkfontscale
%{_mandir}/man1/mkfontscale.*
