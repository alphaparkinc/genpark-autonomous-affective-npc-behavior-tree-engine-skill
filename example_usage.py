from client import AutonomousAffectiveNpcBehaviorTreeEngineClient

def main():
    client = AutonomousAffectiveNpcBehaviorTreeEngineClient()
    res = client.update_npc_cognitive_state('npc_blacksmith_garrick', 'I brought the rare star-metal ore from the volcano summit.')
    print('NPC Turn ID: ' + res['cognitive_turn_id'] + ' (' + res['npc_id'] + ')')
    print('Emotions: ' + str(res['affective_state']) + ' | Goal: ' + res['active_goal'])
    print('Dialogue: "' + res['dialogue_response'] + '"')
    print('Audio Stream: ' + res['speech_audio_stream_url'] + ' (Latency: ' + str(res['turn_latency_ms']) + 'ms)')

if __name__ == '__main__':
    main()
