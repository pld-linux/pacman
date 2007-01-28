Summary:	PLD Package Manager
Summary(pl):	Zarz±dca pakietów PLD
Name:		pacman
Version:	0.1
Release:	4
License:	GPL v2
Group:		Applications
Source0:	http://team.pld-linux.org/~wolf/pacman/%{name}-%{version}.tar.bz2
# Source0-md5:	9439f1f7eca242e74c9a80322cdb38d7
URL:		http://team.pld-linux.org/~wolf/pacman/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	boost-filesystem-devel
BuildRequires:	boost-regex-devel
BuildRequires:	libpi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Package Manager.

%description -l pl
Zarz±dca pakietów PLD.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub admin/
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install src/%{name} $RPM_BUILD_ROOT%{_bindir}
install src/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
