%define fname %{name}_%{version}
%define libname %mklibname %name

Summary:		A test tool for alsa mixer implementations
Name:		    alsamixertest
Version:		48.11
Release:		4
Source0:		https://launchpad.net/~diwic/+archive/ppa/+files/%{fname}.tar.gz
License:		GPLv3
Group:		Sound
Url:		https://thread.gmane.org/gmane.comp.audio.pulseaudio.general/7542
BuildRequires:	pkgconfig(fftw3)
BuildRequires:  pkgconfig(python)

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
%autopatch -p1

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
