import { Component } from '@angular/core';
import { MatTabGroup, MatTab } from '@angular/material/tabs';
import { SimulatorComponent } from '../simulator/simulator.component';

@Component({
  standalone: true,
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrl: './header.component.css',
  imports: [
    MatTab,
    MatTabGroup,
    SimulatorComponent,
  ]
})
export class HeaderComponent {
  title: string = "Space And Rocketry Calculator SpARC"
}
