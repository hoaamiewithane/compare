LOOKER_TO_COGNOS = {
    'Parent Company Code': 'MST Parent Company Code',
    'Lease Term Code': 'Term Code',
    'Lessor Name': 'Lessor Name',
    'Contract Number': 'Contract No.',
    'Agreement Number': 'AGMT No.',
    'EQ Type Size Code': 'TP/SZ Code',
    'Rates - Per Diem': 'Per diem',
    'Rates - Sublease Per Diem': 'Sublease per diem',
    'Rates - Total Per Diem': 'Total per diem',
    'On Hire Date': 'On-Hire Date',
    'Lease Effective Start Date': 'Lease Start Date',
    'Lease Effective Start Calendar Year Month': 'Lease Start Month',
    # 'Lease Effective Start Fiscal Year': 'Lease Start Year',
    'Lease Effective End Date': 'Lease End Date',
    'Lease Effective End Calendar Year Month': 'Lease End Month',
    # 'Lease Effective End Fiscal Year': 'Lease End Year',
    'Build Down Fiscal Year': 'Expiry Year (Build Down)',
    'Minimum Binding Period From Date': 'Min Binding Period Date (From)',
    'Minimum Binding Period To Date': 'Min Binding Period Date (To)',
    'Container Number': 'Container No.',
    'EQ Manufacture Date': 'Year Build Date',
    'Reefer Maker': 'Reefer Maker',
    'Reefer Model Number': 'Model No.'
}

COGNOS_TO_LOOKER = {v: k for k, v in LOOKER_TO_COGNOS.items()}
