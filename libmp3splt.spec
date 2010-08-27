# disable str fmt check temporarily to get the package build (wally 08/2010)
%define Werror_cflags %nil

%define oname	mp3splt
%define major	0
%define libname	%mklibname %{oname} %{major}
%define develname	%mklibname -d %{oname}

Name:		libmp3splt
Version:	0.5.9
Release:	%mkrel 1
Summary:	Library to split MP3 and Ogg Files
Source0:	http://prdownloads.sourceforge.net/mp3splt/%{name}-%{version}.tar.bz2
URL:		http://mp3splt.sourceforge.net
Group:		System/Libraries
License:	GPLv2+
BuildRoot:	%{_tmppath}/build-%{name}-%{version}
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
BuildRequires:	libid3tag-devel
BuildRequires:	zlib-devel
BuildRequires:	glibc-devel
BuildRequires:	libltdl-devel

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

%description -n %{develname}
This package contains development files for the mp3splt project.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --disable-rpath
%make

%install
%makeinstall_std

# we don't want these
rm -rf %{buildroot}%{_libdir}/libmp3splt.{a,la}
rm -rf %{buildroot}%{_libdir}/libmp3splt/*.{a,la}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*
%{_libdir}/%{name}
%exclude %{_libdir}/%{name}/libsplt_*.so

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/%{name}/libsplt_*.so
%{_datadir}/aclocal/%{oname}.m4