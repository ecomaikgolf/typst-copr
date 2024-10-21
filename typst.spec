Name:       typst
Version:    0.12.0
Release:    2
Summary:    A new markup-based typesetting system that is powerful and easy to learn.

License:    Apache-2.0
URL:        https://github.com/typst/typst
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

%if 1%{?rhel}
BuildRequires: rust-toolset
%else
BuildRequires: rust-packaging
%endif
BuildRequires: openssl 
BuildRequires: openssl-libs
BuildRequires: perl


%description
A new markup-based typesetting system that is powerful and easy to learn.


%prep
%autosetup


%build
cargo build -p typst-cli --release --all-features --locked


%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/typst %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
* Mon Oct 21 2024 Ernesto Martínez <me@ecomaikgolf.com>

- Added rhel-based build support

* Mon Oct 21 2024 Ernesto Martínez <me@ecomaikgolf.com>

- Removed autorelease and autochangelog due to RHEL 8,9 and OpenSUSE builds
