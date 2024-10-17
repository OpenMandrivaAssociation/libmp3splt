%define oname	mp3splt
%define major	0
%define libname	%mklibname %{oname} %{major}
%define develname	%mklibname -d %{oname}

Name:		libmp3splt
Version:	0.9.2
Release:	2
Summary:	Library to split MP3 and Ogg Files
Source0:	http://prdownloads.sourceforge.net/mp3splt/%{name}-%{version}.tar.gz
URL:		https://mp3splt.sourceforge.net
Group:		System/Libraries
License:	GPLv2+
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	libtool-devel
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	doxygen

%description
The mp3Splt project provides utilities to split mp3 and ogg files,
by selecting a begin and an end time position, without decoding.
It is very useful to split large mp3/ogg into smaller files,
or to split entire albums to obtain original tracks.
To split an album, the split points and filenames can be selected
manually or automatically from CDDB (internet or a local file),
or from .cue files.

It supports automatic silence detection, which can be used
to adjust cddb/cue split points. It is also possible to extract
tracks from Mp3Wrap or AlbumWrap files in a few seconds.

The mp3splt project is divided in 3 parts:
libmp3splt, mp3splt and mp3splt-gtk.

%package -n %{libname}
Summary:	Library to split MP3 and Ogg Files
Group:		System/Libraries

%description -n %{libname}
Library to split mp3 and ogg files selecting a begin and an end time position,
without decoding. It's very useful to split large mp3/ogg to make smaller
files or to split entire albums to obtain original tracks.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains development files for the mp3splt project.

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%find_lang %{name}0

%files -n %{libname} -f %{name}0.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/%{name}.so.%{major}*
%dir %{_libdir}/%{name}0
%{_libdir}/%{name}0/libsplt_*.so.%{major}*

%files -n %{develname}
%doc %{_docdir}/libmp3splt/doxygen
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}0/libsplt_*.so
