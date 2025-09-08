# GitHub Enterprise Options for Businesses

GitHub offers two main enterprise-level solutions: **GitHub Enterprise Cloud** (hosted SaaS) and **GitHub Enterprise Server** (self-hosted/on-premises or cloud VM). Both are designed for large organizations needing advanced security, compliance, and scale. Requirements and setup differ significantly between the two models.

---

## 🏢 1. GitHub Enterprise Cloud (Hosted SaaS)

**Best For:**
Businesses that want zero infrastructure management, fast onboarding, and out-of-the-box security & compliance.

**Key Requirements:**
- **Organization Ownership:** Must be a GitHub org owner. Existing orgs can upgrade.
- **Subscription:** Purchase GitHub Enterprise plan (includes Actions minutes, storage, SLA). Start with a free 30-day trial or contact sales for invoicing/data residency. Features include 50,000 Actions minutes/month, 50 GB Packages storage, and 99.9% monthly uptime.
- **Browser/Client:** Use latest Chrome, Firefox, Edge, or Safari. Any modern Git client for repo access.
- **Best Practices:**
  - Minimize org count for collaboration.
  - Assign multiple org owners.
  - Set policies for compliance and security.
  - Avoid user-owned repos for business work.
  - Choose managed user identities if needed.
- **No Hardware/OS Prerequisites.** Everything is managed by GitHub. Data residency options available for EU, Australia, US (with more regions planned).

**Setup Steps:**
1. Sign up for a free 30-day trial.
2. Choose enterprise type (personal accounts or managed users) during trial setup.
3. For managed users, select data residency region if needed.
4. Go to GitHub Settings > Organizations > [Your Org] > Billing and Licensing.
5. Click "Upgrade to enterprise account."
6. Enter a name/slug for your enterprise account.
7. Confirm/upgrade—ownership, billing, and policies transfer automatically.
8. Configure SSO (SAML), spending limits, and enterprise policies.
9. All features (Actions, Packages, Copilot, etc.) managed via enterprise dashboard.

---

## 🖥️ 2. GitHub Enterprise Server (Self-Hosted)

**Best For:**
Organizations with strict compliance/regulatory requirements for on-premises control.

**General Prerequisites:**
- **License:** Obtain a GitHub Enterprise license file (45-day free trial available).
- **Platform:** VMware ESXi, Microsoft Hyper-V, OpenStack KVM, AWS, Azure, GCP (x86-64 only).
- **OS:** Self-contained Linux-based appliance (no third-party OS mods).
- **Admin Skills:** Linux admin experience recommended.
- **Networking/Security:** Managed by you (firewall, VPN, IAM, backups).
- **Supported Browsers:** Latest versions of Chrome/Firefox/Edge/Safari.
- **Backups:** Use GitHub Backup Utilities or configure replication.

**Hardware Recommendations (Production):**
As of GHES 3.15+, root disk minimum is 400 GB. Add 25% CPU/memory for features like Actions/Code Security. Use high-performance SSDs with low latency.

| User Licenses | vCPUs | Memory | Root Storage | Data Storage | IOPS |
|---------------|-------|--------|--------------|--------------|------|
| Trial (≤10) | 4 | 32 GB | 400 GB | 500 GB | 600 |
| Up to 1,000 | 8 | 48 GB | 400 GB | 500 GB | 3,000|
| 1,000–3,000 | 16 | 64 GB | 400 GB | 1,000 GB | 6,000|
| 3,000–5,000 | 32 | 128 GB | 400 GB | 1,500 GB | 9,000|
| 5,000–8,000 | 48 | 256 GB | 400 GB | 3,000 GB |12,000|
| 8,000–10,000+ | 64 | 512 GB | 400 GB | 5,000 GB |15,000|

- **Root Storage:** 400GB (200GB usable, rest for upgrades).
- **Data Storage:** Separate volume. Monitor I/O (queue, utilization, latency).
- **Network:** Elastic IP recommended; high bandwidth for large repos/Actions.
- **Clustering:** Supported; provision extra resources for replicas/high availability.

**Setup Steps (e.g., on AWS):**
1. Provision VM per hardware table (e.g., m6i.2xlarge for 1,000 users).
2. Attach storage volumes, set security groups.
3. Download/upload OVA or AMI.
4. Configure via web Management Console.
5. Apply license, set up authentication/policies.

---

## 📝 Decision Factors

- **Enterprise Cloud:**
  - Pros: Fast setup, no infra, built-in upgrades/security, best for most businesses. Enhanced data residency (EU starting Oct 2024, AU/US available).
  - Cons: Less control over data location (but has residency options).

- **Enterprise Server:**
  - Pros: Full control over data/compliance; can run fully air-gapped. Latest (3.17, Jun 2025) enhances deployment, monitoring, code security.
  - Cons: Requires infrastructure, Linux/VM admin, more maintenance.

For details/pricing, visit [GitHub Enterprise Plans](https://github.com/pricing) or contact GitHub Sales.

---

_Last updated: 2025-09-08_