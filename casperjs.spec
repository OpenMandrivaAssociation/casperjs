%define name casperjs
%define rel RC1
%define version 1.0.0
%define release 0.%{rel}

Summary: Navigation scripting and testing utility for PhantomJS
Name:    %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}-%{rel}.tar.gz
Patch0:  casperjs-path-1.0.0.patch
License: MIT
Group:   System/Libraries
Url:     http://casperjs.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: python, phantomjs >= 1.5

%description
CasperJS is an open source navigation scripting & testing utility
written in Javascript and based on PhantomJS - the scriptable headless
WebKit engine. It eases the process of defining a full navigation
scenario and provides useful high-level functions, methods & syntactic
sugar for doing common tasks such as:

* defining & ordering browsing navigation steps
* filling & submitting forms
* clicking & following links
* capturing screenshots of a page (or part of it)
* testing remote DOM
* logging events
* downloading resources, including binary ones
* writing functional test suites, saving results as JUnit XML
* scraping Web contents

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%install
%__rm -rf %{buildroot}
%__install -m 755 -d %{buildroot}%{_bindir}
%__install -m 755 -d %{buildroot}%{_datadir}/casperjs/modules/vendors

%__install -m 755 bin/casperjs %{buildroot}%{_bindir}/
%__install -m 644 bin/usage.txt %{buildroot}%{_datadir}/casperjs/
%__install -m 644 package.json %{buildroot}%{_datadir}/casperjs/
%__install -m 644 bin/bootstrap.js %{buildroot}%{_datadir}/casperjs/
for f in `find modules -type f`; do
%__install -m 644 $f %{buildroot}%{_datadir}/casperjs/$f
done

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG.md LICENSE.md README.md samples/
%_bindir/casperjs
%_datadir/casperjs/*
