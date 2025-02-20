Name:       typst
Version:    0.13.0
Release:    1
Summary:    A new markup-based typesetting system that is powerful and easy to learn.

License:    Apache-2.0
URL:        https://github.com/typst/typst
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

%global debug_package %{nil}

BuildRequires: rust-packaging
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
* Thu Feb 20 2025 Ernesto Martínez <me@ecomaikgolf.com>

- typst 0.13.0

* Mon Oct 21 2024 Ernesto Martínez <me@ecomaikgolf.com>

- Rollback rhel-based build support
- Undefine debug_package macro

* Mon Oct 21 2024 Ernesto Martínez <me@ecomaikgolf.com>

- Added rhel-based build support

* Mon Oct 21 2024 Ernesto Martínez <me@ecomaikgolf.com>

- Removed autorelease and autochangelog due to RHEL 8,9 and OpenSUSE builds
