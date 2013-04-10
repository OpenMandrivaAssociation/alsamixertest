%define fname %{name}_%{version}
%define libname %mklibname %name

Summary:		A test tool for alsa mixer implementations
Name:			alsamixertest
Version:		48.11
Release:		2
Source0:		https://launchpad.net/~diwic/+archive/ppa/+files/%{fname}.tar.gz
License:		GPLv3
Group:		Sound
Url:		http://thread.gmane.org/gmane.comp.audio.pulseaudio.general/7542
BuildRequires:	pkgconfig(fftw3)
%py_requires -d

%description
A small script which tests whether the ALSA mixer lives up to PulseAudio's (and
other advanced ALSA clients) expectations. If you are familiar with dbmeasure
or dbverify by Lennart Poettering, this application's purpose is very similar,
but this one is hopefully easier to set up, more user friendly, and also tests
that the names of the volume controls are correct.

My hope is that this will aid as a debugging tool for all these
"everything below 20% of my speaker is muted, and then 21% blows my speakers"
bugs.

To use the tool, you'll need some kind of loopback. You can e g use a loopback
cable and connect that between line in and line out, or test your laptop's
internal speakers with your laptop's internal mic (just stop humming when you
do so :-) ). Just set up the recording levels appropriately.

When it is installed, run "alsamixertest -r" for a small tutorial and
"alsamixertest -h" for command line options help.

%prep
%setup -q
%apply_patches

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/%{name}
%{_datadir}/%{name}


%changelog
* Wed Nov 03 2010 Funda Wang <fwang@mandriva.org> 48.11-2mdv2011.0
+ Revision: 592779
- rebuild for py 2.7

* Sat Oct 02 2010 Colin Guthrie <cguthrie@mandriva.org> 48.11-1mdv2011.0
+ Revision: 582509
- New version: 48.11

* Wed Sep 29 2010 Colin Guthrie <cguthrie@mandriva.org> 47.14-2mdv2011.0
+ Revision: 582053
- Fix spec name (copy/paste error)
- Fix license after confirming with author

* Mon Sep 27 2010 Colin Guthrie <cguthrie@mandriva.org> 47.14-1mdv2011.0
+ Revision: 581257
- import alsamixertest

