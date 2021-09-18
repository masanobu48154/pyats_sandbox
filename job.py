import os

from genie.harness.main import gRun

def main():
    test_path = os.path.dirname(os.path.abspath(__file__))

    gRun(mapping_datafile=os.path.join(test_path, 'map.yaml'),
        pts_datafile=os.path.join(test_path, 'pts.yaml'),
        trigger_datafile=os.path.join(test_path, 'trigger.yaml'),
        verification_datafile=os.path.join(test_path, 'verify.yaml'),
        pts_features=['platform', 'bgp', 'interface'],
        verification_uids=['Verify_IpInterfaceBrief', 'Verify_BgpAllSummary'],
        trigger_uids=['TriggerUnconfigConfigBgp',  'TriggerModifyLoopbackInterfaceIp']
    )
