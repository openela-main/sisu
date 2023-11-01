# Release type, either "milestone" or "release"
%global reltype release
#global reltag .M1

Name:           sisu
Epoch:          1
Version:        0.3.3
Release:        6%{?dist}
Summary:        Eclipse dependency injection framework
# sisu is EPL-1.0
# bundled asm is BSD
License:        EPL-1.0 and BSD
URL:            http://eclipse.org/sisu

Source0:        http://git.eclipse.org/c/%{name}/org.eclipse.%{name}.inject.git/snapshot/%{reltype}s/%{version}%{?reltag}.tar.bz2#/org.eclipse.%{name}.inject-%{version}%{?reltag}.tar.bz2
Source1:        http://git.eclipse.org/c/%{name}/org.eclipse.%{name}.plexus.git/snapshot/%{reltype}s/%{version}%{?reltag}.tar.bz2#/org.eclipse.%{name}.plexus-%{version}%{?reltag}.tar.bz2

Source100:      %{name}-parent.pom
Source101:      %{name}-inject.pom
Source102:      %{name}-plexus.pom

Patch0:         %{name}-OSGi-import-guava.patch
Patch2:         %{name}-ignored-tests.patch
Patch3:         %{name}-osgi-api.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.inject.extensions:guice-servlet)
BuildRequires:  mvn(com.google.inject:guice::no_aop:)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.testng:testng)

Provides:       bundled(objectweb-asm)


%description
Java dependency injection framework with backward support for plexus and bean
style dependency injection.

%package        inject
Summary:        Sisu inject
Obsoletes:      %{name}-tests < 1:0.3.2-5

%description    inject
This package contains %{summary}.

%package        plexus
Summary:        Sisu Plexus

%description    plexus
This package contains %{summary}.

%package        javadoc
Summary:        API documentation for Sisu

%description    javadoc
This package contains %{summary}.

%prep
%setup -q -c -T
tar xf %{SOURCE0} && mv %{reltype}s/* sisu-inject && rmdir %{reltype}s
tar xf %{SOURCE1} && mv %{reltype}s/* sisu-plexus && rmdir %{reltype}s

cp %{SOURCE100} pom.xml
cp %{SOURCE101} sisu-inject/pom.xml
cp %{SOURCE102} sisu-plexus/pom.xml

%patch0
%patch2
%patch3

%pom_xpath_set -r /pom:project/pom:version %{version}

%mvn_file ":{*}" @1
%mvn_package ":*{inject,plexus}" @1
%mvn_package : __noinstall
%mvn_alias :org.eclipse.sisu.plexus org.sonatype.sisu:sisu-inject-plexus

%build
%mvn_build

%install
%mvn_install

%files inject -f .mfiles-inject
%doc sisu-inject/LICENSE.txt

%files plexus -f .mfiles-plexus

%files javadoc -f .mfiles-javadoc
%doc sisu-inject/LICENSE.txt


%changelog
* Tue Jul 24 2018 Michael Simacek <msimacek@redhat.com> - 1:0.3.3-6
- Declare bundled objectweb-asm
- Fix license tag to include BSD for asm

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  2 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.3.3-4
- Update license tag

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Michael Simacek <msimacek@redhat.com> - 1:0.3.3-1
- Update to upstream version 0.3.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.3.2-6
- Restore alias for org.sonatype.sisu:sisu-inject-plexus

* Sun Jan 29 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.3.2-5
- Build without Tycho
- Remove sisu-tests subpackage
- Drop old obsoletes

* Mon Feb 22 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.3.2-4
- Add alias for org.sonatype.sisu:sisu-inject-plexus

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.3.2-2
- Remove unneeded patch

* Wed Sep 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.3.2-1
- Update to upstream version 0.3.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.3.1-1
- Update to upstream version 0.3.1

* Thu Apr 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.3.0-2
- Install test artifacts

* Mon Feb 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.3.0-1
- Update to upstream version 0.3.0

* Wed Feb 18 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.3.0-0.2.M1
- Unbundle ASM
- Resolves: rhbz#1085903

* Wed Feb  4 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.3.0-0.1.M1
- Update to upstream milestone 0.3.0.M1

* Tue Sep 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-10
- Port to plexus-utils 3.0.18

* Thu Sep 18 2014 Michal Srb <msrb@redhat.com> - 1:0.2.1-9
- Rebuild to fix metadata
- Remove explicit Requires

* Fri Sep 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-8
- Update to latest XMvn version
- Enable tests

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-7
- Fix build-requires on sonatype-oss-parent

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-5
- Install JARs and POMs only

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-4
- Build with XMvn 2.0.0

* Wed May 07 2014 Michael Simacek <msimacek@redhat.com> - 1:0.2.1-3
- Build with Java 8

* Wed Apr 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-2
- Import guava in OSGi manifest

* Tue Apr 22 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-1
- Update to upstream version 0.2.1
- Remove patch for Eclipse bug 429369

* Wed Apr 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-5
- Update upstream patch for bug 429369
- Force usage of Java 1.7

* Mon Mar  3 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-4
- Revert upstream feature which introduced a regression
- Resolves: rhbz#1070915

* Thu Feb 20 2014 Michal Srb <msrb@redhat.com> - 1:0.2.0-3
- Remove R on cdi-api

* Thu Feb 20 2014 Michal Srb <msrb@redhat.com> - 1:0.2.0-2
- Update BR/R for version 0.2.0
- Enable tests

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-1
- Update to upstream version 0.2.0

* Wed Dec  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.1.1-1
- Update to upstream version 0.1.1

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.1.0-1
- Update to upstream version 0.1.0

* Wed Oct 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.7.M5
- Rebuild to regenerate broken POMs
- Related: rhbz#1021484

* Fri Oct 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.6.M5
- Don't inject pom.properties

* Wed Sep 25 2013 Michal Srb <msrb@redhat.com> - 1:0.0.0-0.5.M5
- Update to upstream version 0.0.0.M5
- Install EPL license file
- Inject pom.properties
- Regenerate BR
- Add R

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.4.M4
- Update to XMvn 1.0.0

* Tue Aug 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.3.M4
- Obsolete sisu main package, resolves: rhbz#996288

* Tue Jul 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.2.M4
- Remove unneeded provides and compat symlinks

* Mon Jul 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.1.M4
- Update to upstream version 0.0.0.M4

* Wed Mar 27 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.0-8
- Remove unneeded animal-sniffer BuildRequires
- Add forge-parent to BuildRequires to ensure it's present

* Thu Mar 14 2013 Michal Srb <msrb@redhat.com> - 2.3.0-7
- sisu-inject-bean: add dependency on asm
- Fix dependencies on javax.inject and javax.enterprise.inject
- Remove bundled JARs and .class files from tarball

* Thu Feb  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-6
- Add ASM dependency only to a single module, not all of them
- Disable animal-sniffer plugin
- Don't generate auto-requires for optional dependencies

* Wed Feb 06 2013 Tomas Radej <tradej@redhat.com> - 2.3.0-5
- Added BR on animal-sniffer

* Tue Feb 05 2013 Tomas Radej <tradej@redhat.com> - 2.3.0-4
- Split into subpackages
- Build with new macros
- Unbundled objectweb-asm

* Wed Dec  5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-3
- Fix OSGi __requires_exclude

* Wed Dec  5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-2
- Disable OSGi auto-requires: org.sonatype.sisu.guava

* Mon Dec  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-1
- Update to upstream version 2.3.0

* Tue Jul 24 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.3-6
- Convert patches to POM macros

* Mon Jul 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.3-5
- Fix license tag

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.3-2
- Add backward compatible package path for lifecycles
- Remove temporary BRs/Rs

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.3-1
- Update to latest upstream 2.2.3 (#683795)
- Add forge-parent to Requires
- Rework spec to be more simple, update patches

* Tue Mar  1 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1.1-2
- Add atinject into poms as dependency

* Mon Feb 28 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1.1-1
- Update to 2.1.1
- Update patch
- Disable guice-eclipse for now

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.3.2-1
- Update to latest upstream version
- Versionless jars & javadocs

* Mon Oct 18 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.2-2
- Add felix-framework BR

* Thu Oct 14 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.2-1
- Initial version of the package
